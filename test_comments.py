import pytest
from app import app, db
from models import Comment, Task

@pytest.fixture(scope="module")
def test_client():
    # Flask provides a way to test apps without running a server
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            # Add one sample task
            db.session.add(Task(title="Sample Task"))
            db.session.commit()
        yield testing_client
        # Teardown: drop tables after test
        with app.app_context():
            db.drop_all()


def test_add_comment(test_client):
    # Send POST request
    response = test_client.post(
        '/api/tasks/1/comments',
        json={"comment_text": "Hello"}
    )

    # ✅ Check status code
    assert response.status_code == 201

    # ✅ Parse response JSON
    data = response.get_json()
    assert data["comment_text"] == "Hello"
    assert data["task_id"] == 1

    # ✅ Check DB entry
    with app.app_context():
        comment = Comment.query.first()
        assert comment is not None
        assert comment.comment_text == "Hello"
        assert comment.task_id == 1
