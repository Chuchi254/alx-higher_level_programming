#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
	if (!PyList_Check(p)) {
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i =0; i < size; i++) {
		PyObject *item = ((PyListObject *)p)->ob_item[i];
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item)) {
			print_python_bytes(item);
		} else if (PyFloat_Check(item)) {
			print_python_float(item);
		}
	}
}

void print_python_bytes(PyObject *p) {
	if (!PyBytes_Check(p)) {
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	char *str = ((PyBytesObject *)p)->ob_sval;
	Py_ssize_t i, limit = size < 10 ? size : 10;

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes: ", limit);
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

	double value = ((PyFloatObject *)p)->ob_fval;
	printf("[.] float object info\n");
	printf(" value: %g\n", value);
}
