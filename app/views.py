from flask import Blueprint, g, jsonify, request

from app.auth import is_admin, login_required

bp = Blueprint("notes", __name__)
NOTES: list[dict] = []


@bp.get("/notes")
@login_required
def list_notes():
    page = max(int(request.args.get("page", 1)), 1)
    per_page = min(max(int(request.args.get("per_page", 20)), 1), 100)
    mine = [n for n in NOTES if n["owner"] == g.user.id]
    return jsonify(mine[(page - 1) * per_page : page * per_page])


@bp.get("/admin/export")
@login_required
def export_all():
    if not is_admin(g.user):
        return jsonify(error="forbidden"), 403
    return jsonify(NOTES)
