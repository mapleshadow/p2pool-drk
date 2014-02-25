#include <Python.h>

#include "dark.h"

static PyObject *quark_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    dark_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    dark_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef QuarkMethods[] = {
    { "getPoWHash", quark_getpowhash, METH_VARARGS, "Returns the proof of work hash using quark hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef QuarkModule = {
    PyModuleDef_HEAD_INIT,
    "dark_hash",
    "...",
    -1,
    QuarkMethods
};

PyMODINIT_FUNC PyInit_dark_hash(void) {
    return PyModule_Create(&QuarkModule);
}

#else

PyMODINIT_FUNC initdark_hash(void) {
    (void) Py_InitModule("dark_hash", QuarkMethods);
}
#endif
