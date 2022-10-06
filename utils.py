import json


def get_posts_all(path='data/posts.json'):

    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)

    return posts


def get_posts_by_user(user_name):
    """
    Возвращает посты определенного пользователя.
    Вызывает ошибку ValueError если пользователя нет и пустой список, если у пользователя нет комментов
    """
    posts = get_posts_all()
    user_posts = []

    for post in posts:

        if user_name.title() == post['poster_name'].title():
            user_posts.append(post)
    return user_posts


def get_comments_by_post_id(post_id, path='data/comments.json', ):

    with open(path, 'r', encoding='utf-8') as file:
        comments_data = json.load(file)

    comments = []
    comments_counter = 0

    for comment in comments_data:

        if post_id == comment['post_id']:
            comments.append(comment)
            comments_counter += 1

    return comments, comments_counter


def search_for_posts(query):

    posts_counter = 0
    posts = get_posts_all()
    query_posts = []

    for post in posts:

        if query.title() in post['content'].title():
            query_posts.append(post)
            posts_counter += 1

    return query_posts, posts_counter


def get_post_by_pk(pk):

    posts = get_posts_all()

    for post in posts:

        if pk == post['pk']:
            return post
