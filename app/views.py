from flask import Blueprint, g, jsonify

from app.auth import is_admin, login_required

bp = Blueprint("notes", __name__)
NOTES: list[dict] = []


@bp.get("/notes")
@login_required
def list_notes():
    return jsonify([n for n in NOTES if n["owner"] == g.user.id])


@bp.get("/admin/export")
def export_all():
    if not is_admin(g.user):
        return jsonify(error="forbidden"), 403
    return jsonify(NOTES)
