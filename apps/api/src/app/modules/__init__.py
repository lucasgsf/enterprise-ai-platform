"""Bounded contexts of the modular monolith.

Each submodule is a domain boundary (see ADR-0001). Modules communicate only through
explicit public interfaces, never importing each other's internals. Most are empty
placeholders, to be filled in their respective releases.
"""
