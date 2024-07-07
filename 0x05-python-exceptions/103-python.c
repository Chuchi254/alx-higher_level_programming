#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t i;

	if (!PyList_Check(p)) {
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*} Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++) {
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item)) {
			print_python_bytes(item);
		} else if (PyFloat_Check(item)) {
			print_python_float(item);
		}
	}
}

void print_python_bytes(PyObject *p) {
	if (!PyBytes_Check(p)) {
		printf("[ERROR] Invalid Bytes object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *str = PyBytes_AsString(p);
	Py_ssize_t i, limit = size < 10 ? size : 10;

	printf("[.] bytes object info\n");
	printf(" size: %zd\n", size);
	printf(" trying string: %s\n", str);
	printf(" first %zd bytes: ", limit);
	for (i = 0; i < limit; i++) {
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("\n");
}

void print_python_float(PyObject *p) {
	if (!PyFloat_Check(p)) {
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);
	printf("[.] float object info\n");
	printf(" value: %f\n", value);
}
