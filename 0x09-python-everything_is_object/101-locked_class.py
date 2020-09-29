#!/usr/bin/python3
""" class to avoid to create diferent atributtes
"""


class LockedClass:
    """new class control slot"""
    __slots__ = "first_name"
