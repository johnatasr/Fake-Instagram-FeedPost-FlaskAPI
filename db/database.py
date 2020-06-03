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

    cursor.execute('INSERT OR REPLACE INTO posts VALUES(1, "https://ibb.co/album/bbX6pK", "https://ibb.co/gTTKJG4", "john123", "Nice Place", 1, 10);')
    cursor.execute('INSERT OR REPLACE INTO posts VALUES(2, "https://ibb.co/album/bbX6pK", "https://ibb.co/pZSvY88", "jessica_k10", "Amazing", 1, 15);')
    cursor.execute('INSERT OR REPLACE INTO posts VALUES(3, "https://ibb.co/album/bbX6pK", "https://ibb.co/xLD2g5N", "barbara@happy", "Cool", 1, 3);')
    cursor.execute('INSERT OR REPLACE INTO posts VALUES(4, "https://ibb.co/album/bbX6pK", "https://ibb.co/KrWtW01", "michaelmiller68", "Take that", 0, 0);')
    cursor.execute('INSERT OR REPLACE INTO posts VALUES(5, "https://ibb.co/album/bbX6pK", "https://ibb.co/7C9V6hy", "hudson1970", "Other Place", 1, 58);')

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

    print('Database successfully created and populated with data!')