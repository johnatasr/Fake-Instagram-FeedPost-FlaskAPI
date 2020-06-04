import sqlite3


def create_database(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    create_comment_table = '{}{}{}'.format(
                        'CREATE TABLE IF NOT EXISTS',
                        ' comments(id INTEGER PRIMARY KEY,',
                        ' login text NOT NULL, text_comment text NOT NULL);'
                        )

    cursor.execute(create_comment_table)

    create_post_table ='{}{}{}{}{}{}{}'.format(
                          'CREATE TABLE IF NOT EXISTS',
                          ' posts(id INTEGER PRIMARY KEY,',
                          ' url_perfil text, url_photo text,',
                          ' login_user text,',
                          ' comment text,',
                          ' liked INTEGER NOT NULL DEFAULT 0 CHECK(liked IN (0,1)),',
                          ' likers INTEGER NOT NULL);',
                          )
    cursor.execute(create_post_table)

    create_post_comment_table = '{}{}{}'.format(
        'CREATE TABLE IF NOT EXISTS',
        ' post_comments_ref(post_ref INTEGER NOT NULL,',
        ' comment_ref INTEGER NOT NULL, PRIMARY KEY(post_ref, comment_ref));'
    )

    cursor.execute(create_post_comment_table)

    cursor.execute('INSERT OR REPLACE INTO comments VALUES(1, "barbara123", "Amazing place");')
    cursor.execute('INSERT OR REPLACE INTO comments VALUES(2, "jessica_k10", "Cool Budy");')
    cursor.execute('INSERT OR REPLACE INTO comments VALUES(3, "jessica_k10", "Try again soon");')
    cursor.execute('INSERT OR REPLACE INTO comments VALUES(4, "Marcos@167", "LOL");')
    cursor.execute('INSERT OR REPLACE INTO comments VALUES(5, "markZuke", "Owww");')
    cursor.execute('INSERT OR REPLACE INTO comments VALUES(6, "Marcos@167", "Owww Nice Man");')
    cursor.execute('INSERT OR REPLACE INTO comments VALUES(7, "jimmypage123", "My guitar its more useful");')
    cursor.execute('INSERT OR REPLACE INTO comments VALUES(8, "jessica_k10", "Try again soon");')

    cursor.execute('INSERT OR REPLACE INTO posts VALUES(1, "https://i.ibb.co/99RTKVS/Person-Curtis-4x5-e1564616444404.jpg", "https://i.ibb.co/kBd0WZc/paisagem-tropical-wallpaper-1.jpg", "john123", "Nice Place", 1, 10);')
    cursor.execute('INSERT OR REPLACE INTO posts VALUES(2, "https://i.ibb.co/LYHZ5xQ/images.jpg", "https://i.ibb.co/4MHZhGG/Fotos-de-Paisagens-Ipes-Rosa-em-BH-Charles-Torres.jpg", "jessica_k10", "Amazing", 1, 15);')
    cursor.execute('INSERT OR REPLACE INTO posts VALUES(3, "https://i.ibb.co/s5vsjTK/Missing-Persons-Dale-Bozzio-2020.jpg", "https://i.ibb.co/jMMXDdJ/277277-Papel-de-Parede-Bela-Paisagem-de-Campo-1680x1050.jpg", "barbara@happy", "Cool", 1, 3);')
    cursor.execute('INSERT OR REPLACE INTO posts VALUES(4, "https://i.ibb.co/7nJGFCc/images-1.jpg", "https://i.ibb.co/F3KhY7F/Fotos-de-Paisagens-Luzes-de-Brasilia-Charles-Torres.jpg", "michaelmiller68", "Take that", 0, 0);')
    cursor.execute('INSERT OR REPLACE INTO posts VALUES(5, "https://i.ibb.co/R36vMYg/images-2.jpg", "https://i.ibb.co/P6g2gmS/Fotos-de-Paisagens-Natureza-e-Cachoeiras-Charles-Torres.jpg", "hudson1970", "Other Place", 1, 58);')

    cursor.execute('''INSERT INTO post_comments_ref VALUES
                        (1,1), 
                        (1,2), 
                        (2,3), 
                        (2,4), 
                        (2,5), 
                        (3,6), 
                        (4,7), 
                        (5,8), 
                        (5,4) ;''')
    connection.commit()
    connection.close()

    print('Dados sincronizados !  ||  Database Synchronized !')