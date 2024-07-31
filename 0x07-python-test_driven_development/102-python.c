#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>

/**
 * print_python_string - prints information about Python string
 * @p: PyObject string object
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	wchar_t *value;

	setlocale(LC_ALL, "");

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	value = PyUnicode_AsWideCharString(p, &length);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", length);
	printf("  value: %ls\n", value);

	PyMem_Free(value);
}
