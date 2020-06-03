import sqlite3


class PostModel:

    def __init__(self,
                 id: int,
                 url_perfil: str,
                 url_photo: str,
                 login_user: str,
                 comment: str,
                 liked: int,
                 likers: int,
                 comments: list):
        self.id = id
        self.url_perfil = url_perfil
        self.url_photo = url_photo
        self.login_user = login_user
        self.comment = comment
        self.liked = liked
        self.likers = likers
        self.comments = comments

    @staticmethod
    def comments_transform(logins, comments) -> list:
        comments_all = list()
        formated_login = logins.split("-")
        formated_comments = comments.split("-")

        for login, comment in zip(formated_login, formated_comments):
            comment_dic = {
                "login": login,
                "comment": comment
            }
            comments_all.append(comment_dic)

        return comments_all

    @classmethod
    def find_all_posts(cls) -> list:
        posts = list()
        connection = sqlite3.connect('./db/data.db')
        cursor = connection.cursor()
        query = '''SELECT posts.id, url_perfil, url_photo, login_user, comment, liked, likers, GROUP_CONCAT(login, ' - '), GROUP_CONCAT(text_comment, ' - ')
                    FROM posts JOIN post_comments_ref ON post_ref = posts.id 
                    JOIN comments ON comments.id = comment_ref
                    GROUP BY posts.id'''
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                comments = cls.comments_transform(row[7], row[8])
                posts.append(PostModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], comments))
            return posts
        connection.close()

    @classmethod
    def find_post(cls, post: int) -> list:
        posts = list()
        connection = sqlite3.connect('./db/data.db')
        cursor = connection.cursor()
        query = '''SELECT posts.id, url_perfil, url_photo, login_user, comment, liked, likers, GROUP_CONCAT(login, ' - '), GROUP_CONCAT(text_comment, ' - ')
                    FROM posts JOIN post_comments_ref ON post_ref = posts.id 
                    JOIN comments ON comments.id = comment_ref WHERE posts.id = ?
                    GROUP BY posts.id;'''
        result = cursor.execute(query, (post,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                comments = cls.comments_transform(row[7], row[8])
                posts.append(PostModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], comments))
            return posts
        connection.close()

    def json(self) -> dict:
        return {
            'id': self.id,
            'url_perfil': self.url_perfil,
            'url_photo': self.url_photo,
            'login': self.login_user,
            'comment': self.comment,
            'liked': self.liked,
            'likers': self.likers,
            'comments': self.comments
        }
