from flask import Blueprint, request, jsonify
from extensions import db
from models import Comment

comments_bp = Blueprint('comments', __name__, url_prefix='/api')

# CREATE comment (POST)
@comments_bp.route('/tasks/<int:task_id>/comments', methods=['POST'])
def add_comment(task_id):
    data = request.get_json()
    comment_text = data.get('comment_text')
    if not comment_text:
        return jsonify({"error": "Missing comment_text"}), 400

    new_comment = Comment(task_id=task_id, comment_text=comment_text)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({
        "id": new_comment.id,
        "task_id": new_comment.task_id,
        "comment_text": new_comment.comment_text
    }), 201


# READ (GET all comments for a task)
@comments_bp.route('/tasks/<int:task_id>/comments', methods=['GET'])
def get_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([
        {"id": c.id, "task_id": c.task_id, "comment_text": c.comment_text}
        for c in comments
    ])


# UPDATE (PUT)
@comments_bp.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.get_json()
    comment = Comment.query.get_or_404(comment_id)

    comment.comment_text = data.get('comment_text', comment.comment_text)
    db.session.commit()

    return jsonify({
        "id": comment.id,
        "task_id": comment.task_id,
        "comment_text": comment.comment_text
    })


# DELETE
@comments_bp.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted"}), 200
