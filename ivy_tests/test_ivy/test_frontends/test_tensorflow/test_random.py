from hypothesis import strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test


# random_sample
@handle_frontend_test(
    fn_tree="tensorflow.random.uniform",
    shape=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        min_value=1,
        max_value=5,
        min_num_dims=1,
        max_num_dims=1,
    ),
    minval=helpers.ints(min_value=0, max_value=3),
    maxval=helpers.ints(min_value=4, max_value=10),
    dtype=helpers.get_dtypes("float", full=False),
    seed=helpers.ints(min_value=0, max_value=10),
    test_with_out=st.just(False),
)
def test_tensorflow_uniform(
    shape,
    minval,
    maxval,
    dtype,
    seed,
    frontend,
    test_flags,
    fn_tree,
    on_device,
):

    input_dtypes, shape = shape
    helpers.test_frontend_function(
        input_dtypes=input_dtypes,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        test_values=False,
        shape=shape[0],
        minval=minval,
        maxval=maxval,
        dtype=dtype[0],
        seed=seed,
    )


# random_normal
@handle_frontend_test(
    fn_tree="tensorflow.random.normal",
    shape=helpers.get_shape(
        allow_none=False,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
    ),
    mean=st.floats(allow_nan=False, allow_infinity=False, width=32),
    stddev=st.floats(allow_nan=False, allow_infinity=False, width=32, min_value=0),
    dtype=helpers.get_dtypes("float", full=False),
    seed=helpers.ints(min_value=0, max_value=10),
    test_with_out=st.just(False),
)
def test_tensorflow_normal(
    frontend,
    fn_tree,
    on_device,
    shape,
    mean,
    stddev,
    dtype,
    seed,
    test_flags,
):

    helpers.test_frontend_function(
        input_dtypes=dtype,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        test_values=False,
        shape=shape,
        mean=mean,
        stddev=stddev,
        dtype=dtype[0],
        seed=seed,
    )


# random_shuffle
@handle_frontend_test(
    fn_tree="tensorflow.random.shuffle",
    dtype_value=helpers.dtype_and_values(available_dtypes=helpers.get_dtypes("valid")),
    seed=helpers.ints(min_value=0, max_value=10),
    test_with_out=st.just(False),
)
def test_tensorflow_shuffle(
    frontend,
    fn_tree,
    on_device,
    dtype_value,
    seed,
    test_flags,
):
    input_dtypes, values = dtype_value
    helpers.test_frontend_function(
        input_dtypes=input_dtypes,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        test_values=False,
        value=values[0],
        seed=seed,
    )


# random_stateless_uniform
@handle_frontend_test(
    fn_tree="tensorflow.random.stateless_uniform",
    shape=helpers.dtype_and_values(
        available_dtypes=("int64", "int32"),
        min_value=1,
        max_value=5,
        min_num_dims=1,
        max_num_dims=1,
        max_dim_size=9,
    ),
    seed=helpers.dtype_and_values(
        available_dtypes=("int64", "int32"), min_value=0, max_value=10, shape=[2]
    ),
    minmaxval=helpers.get_bounds(dtype="int32"),
    dtype=helpers.array_dtypes(
        available_dtypes=("int32", "int64", "float16", "float32", "float64"),
    ),
    test_with_out=st.just(False),
)
def test_tensorflow_stateless_uniform(
    shape,
    seed,
    minmaxval,
    dtype,
    frontend,
    test_flags,
    fn_tree,
    on_device,
):
    shape_input_dtypes, shape = shape
    seed_input_dtypes, seed = seed

    helpers.test_frontend_function(
        input_dtypes=shape_input_dtypes + seed_input_dtypes,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        test_values=False,
        shape=shape[0],
        seed=seed[0],
        minval=int(minmaxval[0]),
        maxval=int(minmaxval[1]),
        dtype=dtype[0],
    )


# random poisson
@handle_frontend_test(
    fn_tree="tensorflow.random.poisson",
    shape=helpers.get_shape(
        min_num_dims=1,
        max_num_dims=3,
        min_dim_size=1,
        max_dim_size=10,
    ),
    lam=st.one_of(
        st.floats(allow_infinity=False, allow_nan=False, width=32),
        st.lists(
            st.floats(allow_nan=False, allow_infinity=False, width=32),
            min_size=1,
            max_size=10,
        ),
    ),
    dtype=helpers.get_dtypes("float", full=False),
    seed=helpers.ints(min_value=0, max_value=10),
    test_with_out=st.just(False),
)
def test_tensorflow_poisson(
    frontend,
    fn_tree,
    on_device,
    shape,
    lam,
    dtype,
    seed,
    test_flags,
):
    helpers.test_frontend_function(
        input_dtypes=dtype,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        lam=lam,
        shape=shape,
        dtype=dtype[0],
        seed=seed,
        test_values=False,
    )
