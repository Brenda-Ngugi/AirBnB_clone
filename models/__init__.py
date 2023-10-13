"""
reload() from importlib: quickly test changes to a module without
having to exit and restart the Python interpreter
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
