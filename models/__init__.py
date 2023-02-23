#!/usr/bin/python3
"""__init__ file that also imports FileStorage and uses the reload func"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
