from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    notifications = [
        {
        'from': {'user': 'Pontus Blomqvist'},
        'text': 'has responded to your comment X',
        'time': '1 week ago',
        'image': 'images/profile.jpg',
        'color': 'color: #00e664;'
        },
        {
        'from': {'user': 'Eliška Rychetská'},
        'text': 'has responded to your comment X',
        'time': '1 week ago',
        'image': 'images/user1.jpg',
        'color': 'color: #bf279b;'
        },
        {
        'from': {'user': 'Noam Chomsky'},
        'text': 'has responded to your comment X',
        'time': '2 week ago',
        'image': 'images/user3.png',
        'color': 'color: #e67600;'
        }
    ]

    user = {
        'username': 'Pontus Blomqvist',
        'numberofnotifications': len(notifications)
        }

    comments = [
        {
            'author': {'username': 'Eliška Rychetská'},
            'image': 'images/user1.jpg',
            'color': 'color: #bf279b;',
            'comment': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
            'score': '2724',
            'time': '1 week ago'
        },
        {
            'author': {'username': 'Pontus Blomqvist'},
            'image': 'images/profile.jpg',
            'color': 'color: #00e664;',
            'comment': 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...',
            'score': '-5235',
            'time': '1 day ago',
            'response': {
                'username': 'Eliška Rychetská',
                'image': 'images/user1.jpg',
                'color': 'color: #bf279b;',
                'respondto' : 'PontusBlomqvist',
                'comment': 'Aboris nisi ut aliquip ex ea commodo consequat.'},
                'score': '36',
                'time': '2 hours ago'
        },
        {
            'author': {'username': 'Noam Chomsky'},
            'image': 'images/user3.png',
            'color': 'color: #e67600;',
            'comment': 'Et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et',
            'score': '7',
            'time': '21 minutes ago'
        }
    ]
    return render_template('main.html', title='Open Forum', user=user, comments=comments, notifications=notifications)