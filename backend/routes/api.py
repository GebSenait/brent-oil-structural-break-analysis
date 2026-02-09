"""
REST API routes for change point dashboard: returns, prices, events, posterior summary.
"""
from flask import Blueprint, jsonify, request

from backend.services.data_service import (
    get_returns,
    get_prices,
    get_events,
    get_change_point_posterior,
)

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "change-point-dashboard"})


@api.route("/returns", methods=["GET"])
def returns():
    data = get_returns()
    return jsonify({"data": data, "count": len(data)})


@api.route("/prices", methods=["GET"])
def prices():
    data = get_prices()
    return jsonify({"data": data, "count": len(data)})


@api.route("/events", methods=["GET"])
def events():
    category = request.args.get("category")
    data = get_events(category=category)
    return jsonify({"data": data, "count": len(data)})


@api.route("/change-point", methods=["GET"])
def change_point():
    payload = get_change_point_posterior()
    if payload is None:
        return jsonify({"error": "Change point posterior not found. Run Task-2 notebook to generate change_point_posterior.json."}), 404
    return jsonify(payload)
