#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
