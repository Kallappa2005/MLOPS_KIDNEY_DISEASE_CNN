import pathlib
import py_compile
import unittest


class TestProjectSmoke(unittest.TestCase):
    def test_required_runtime_files_exist(self):
        required_files = [
            pathlib.Path("app.py"),
            pathlib.Path("Dockerfile"),
            pathlib.Path("requirements.txt"),
            pathlib.Path("templates/index.html"),
            pathlib.Path("model/model.h5"),
        ]

        missing = [str(file_path) for file_path in required_files if not file_path.exists()]
        self.assertEqual(missing, [], f"Missing required files: {missing}")

    def test_python_files_are_syntax_valid(self):
        ignored_dirs = {".git", ".venv", "venv", "env", "research", "mlruns"}
        py_files = []

        for file_path in pathlib.Path(".").rglob("*.py"):
            if any(part in ignored_dirs for part in file_path.parts):
                continue
            py_files.append(file_path)

        self.assertGreater(len(py_files), 0, "No Python files found for syntax validation")

        compile_errors = []
        for py_file in py_files:
            try:
                py_compile.compile(str(py_file), doraise=True)
            except py_compile.PyCompileError as exc:
                compile_errors.append(f"{py_file}: {exc.msg}")

        self.assertEqual(compile_errors, [], "\n".join(compile_errors))


if __name__ == "__main__":
    unittest.main()
