import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from mySEblog.models import Post
from reviews.models import Review

def get_recommendations(user):
    if not user.is_authenticated:
        return Post.objects.none()
    data = Review.objects.values('created_by', 'post', 'rating')
    df = pd.DataFrame(data)
    df.rename(columns={'created_by': 'created_by_id', 'post': 'post_id'}, inplace=True)

    if df.empty:
        return Post.objects.none()

    user_item_matrix = df.pivot_table(index='created_by_id', columns='post_id', values='rating', fill_value=0)

    if user.id not in user_item_matrix.index:
        return Post.objects.none()

    similarity_matrix = cosine_similarity(user_item_matrix)
    similarity_df = pd.DataFrame(similarity_matrix, index=user_item_matrix.index, columns=user_item_matrix.index)

    similar_users = similarity_df[user.id].sort_values(ascending=False).iloc[1:6]

    similar_users_posts = df[df['created_by_id'].isin(similar_users.index)]

    user_posts = df[df['created_by_id']==user.id]['post_id'].unique()
    recommended_posts_ids = similar_users_posts[~similar_users_posts['post_id'].isin(user_posts)]['post_id'].unique()

    return Post.objects.filter(pk__in=recommended_posts_ids)