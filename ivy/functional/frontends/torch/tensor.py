# global

# local
import ivy
import ivy.functional.frontends.torch as torch_frontend
import ivy.functional.frontends.torch.nn.functional as torch_frontend_nn
from ivy.functional.frontends.numpy.creation_routines.from_existing_data import (
    array as np_frontend_array,
)
from ivy.func_wrapper import with_unsupported_dtypes
from ivy.func_wrapper import with_supported_dtypes
from ivy.functional.frontends.torch.func_wrapper import _to_ivy_array


class Tensor:
    def __init__(self, array, device=None, _init_overload=False):

        if _init_overload:
            self._ivy_array = (
                ivy.array(array) if not isinstance(array, ivy.Array) else array
            )

        else:
            self._ivy_array = ivy.array(
                array, dtype=torch_frontend.float32, device=device
            )

    def __repr__(self):
        return str(self.ivy_array.__repr__()).replace(
            "ivy.array", "ivy.frontends.torch.Tensor"
        )

    # Properties #
    # ---------- #

    @property
    def ivy_array(self):
        return self._ivy_array

    @property
    def device(self):
        return ivy.dev(self.ivy_array)

    @property
    def dtype(self):
        return self.ivy_array.dtype

    @property
    def shape(self):
        return self.ivy_array.shape

    # Setters #
    # --------#

    @ivy_array.setter
    def ivy_array(self, array):
        self._ivy_array = (
            ivy.array(array) if not isinstance(array, ivy.Array) else array
        )

    # Instance Methods #
    # ---------------- #
    def reshape(self, *args, shape=None):
        if args and shape:
            raise TypeError("reshape() got multiple values for argument 'shape'")
        if shape is not None:
            return torch_frontend.reshape(self, shape)
        if args:
            if isinstance(args[0], (tuple, list)):
                shape = args[0]
                return torch_frontend.reshape(self, shape)
            else:
                return torch_frontend.reshape(self, args)
        return torch_frontend.reshape(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def reshape_as(self, other):
        return torch_frontend.reshape(self, other.shape)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def add(self, other, *, alpha=1):
        return torch_frontend.add(self, other, alpha=alpha)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def sub(self, other, *, alpha=1):
        return torch_frontend.sub(self, other, alpha=alpha)

    def chunk(self, chunks, dim=0):
        return torch_frontend.chunk(self, chunks, dim=dim)

    def any(self, dim=None, keepdim=False):
        return torch_frontend.any(self, dim=dim, keepdim=keepdim)

    def all(self, dim=None, keepdim=False):
        return torch_frontend.all(self, dim=dim, keepdim=keepdim)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def add_(self, other, *, alpha=1):
        self.ivy_array = self.add(other, alpha=alpha).ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def subtract_(self, other, *, alpha=1):
        self.ivy_array = self.subtract(other, alpha=alpha).ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def asin(self):
        return torch_frontend.asin(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def asin_(self):
        self.ivy_array = self.asin().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def sum(self):
        return torch_frontend.sum(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def sin(self):
        return torch_frontend.sin(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def sin_(self):
        self.ivy_array = self.sin().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def sinh(self):
        return torch_frontend.sinh(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def sinh_(self):
        self.ivy_array = self.sinh().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def cos(self):
        return torch_frontend.cos(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def cos_(self):
        self.ivy_array = self.cos().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def cosh(self):
        return torch_frontend.cosh(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def cosh_(self):
        self.ivy_array = self.cosh().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arcsinh(self):
        return torch_frontend.arcsinh(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arcsin(self):
        return torch_frontend.arcsin(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arcsin_(self):
        self.ivy_array = self.arcsin().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def atan(self):
        return torch_frontend.atan(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def atan_(self):
        self.ivy_array = self.atan().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "bfloat16")}, "torch")
    def atan2(self, other):
        return torch_frontend.atan2(self, other)

    def view(self, *args, shape=None):
        """
        Reshape Tensor.

        possible arguments are either:
            - size
            - tuple of ints
            - list of ints
            - torch.Size object
            - ints
        Parameters
        ----------
        args:int arguments
        shape: optional shape

        Returns reshaped tensor
        -------
        """
        if shape and not args:
            shape_tup = shape
        elif args and not shape:
            if (
                isinstance(args[0], tuple)
                or isinstance(args[0], list)
                or type(args[0]).__name__ == "Size"
            ) and len(args) == 1:
                shape_tup = args[0]
            else:
                shape_tup = args
        else:
            raise ValueError(
                "View only accepts as argument ints, tuple or list of ints or "
                "the keyword argument size."
            )
        return torch_frontend.reshape(self, shape_tup)

    def float(self, memory_format=None):
        self.ivy_array = ivy.astype(self.ivy_array, ivy.float32, copy=False)
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def asinh(self):
        return torch_frontend.asinh(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def asinh_(self):
        self.ivy_array = self.asinh().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def tan(self):
        return torch_frontend.tan(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def tan_(self):
        self.ivy_array = self.tan().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def tanh(self):
        return torch_frontend.tanh(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def tanh_(self):
        self.ivy_array = self.tanh().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def atanh(self):
        return torch_frontend.atanh(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def atanh_(self):
        self.ivy_array = self.atanh().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arctanh(self):
        return torch_frontend.arctanh(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arctanh_(self):
        self.ivy_array = self.arctanh().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def log(self):
        return torch_frontend.log(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arccosh(self):
        return torch_frontend.arccosh(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def log_(self):
        self.ivy_array = self.log().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def log2(self):
        return torch_frontend.log2(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "bfloat16")}, "torch")
    def relu(self):
        return torch_frontend_nn.relu(self)

    def amax(self, dim=None, keepdim=False):
        return torch_frontend.amax(self, dim=dim, keepdim=keepdim)

    def amin(self, dim=None, keepdim=False):
        return torch_frontend.amin(self, dim=dim, keepdim=keepdim)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def aminmax(self, dim=None, keepdim=False):
        return torch_frontend.aminmax(self, dim=dim, keepdim=keepdim)

    def abs(self):
        return torch_frontend.abs(self)

    def abs_(self):
        self.ivy_array = self.abs().ivy_array
        return self

    def logical_and(self, other):
        return torch_frontend.logical_and(self, other)

    def logical_not(self, *, out=None):
        return torch_frontend.logical_not(self, out=out)

    def logical_or(self, other):
        return torch_frontend.logical_or(self, other)

    def bitwise_not(self):
        return torch_frontend.bitwise_not(self)

    def bitwise_and(self, other):
        return torch_frontend.bitwise_and(self, other)

    def bitwise_or(self, other):
        return torch_frontend.bitwise_or(self, other)

    def bitwise_left_shift(self, other):
        return torch_frontend.bitwise_left_shift(self, other)

    @with_supported_dtypes({"1.11.0 and below": ("integer",)}, "torch")
    def bitwise_or_(self, other):
        self.ivy_array = self.bitwise_or(other).ivy_array
        return self

    def contiguous(self, memory_format=None):
        return torch_frontend.tensor(self)

    def new_ones(self, size, *, dtype=None, device=None, requires_grad=False):
        return torch_frontend.ones(
            size, dtype=dtype, device=device, requires_grad=requires_grad
        )

    def floor(self, *, out=None):
        return torch_frontend.floor(self)

    def new_zeros(self, size, *, dtype=None, device=None, requires_grad=False):
        return torch_frontend.zeros(
            size, dtype=dtype, device=device, requires_grad=requires_grad
        )

    def to(self, *args, **kwargs):
        if len(args) > 0:
            if hasattr(args[0], "ivy_array") or ivy.is_array(args[0]):
                if self.dtype == ivy.dtype(args[0]) and self.device == ivy.dev(args[0]):
                    return self
                else:
                    cast_tensor = self.clone()
                    cast_tensor.ivy_array = ivy.asarray(
                        self.ivy_array,
                        dtype=ivy.dtype(args[0]),
                        device=ivy.dev(args[0]),
                    )
                    return cast_tensor
            if (
                isinstance(args[0], (ivy.Dtype, ivy.NativeDtype))
                or args[0] in ivy._all_ivy_dtypes_str
            ):
                if self.dtype == ivy.as_ivy_dtype(args[0]):
                    return self
                else:
                    cast_tensor = self.clone()
                    cast_tensor.ivy_array = ivy.asarray(self.ivy_array, dtype=args[0])
                    return cast_tensor
            if isinstance(args[0], (ivy.Device, ivy.NativeDevice, str)):
                if isinstance(args[0], str) and not isinstance(
                    args[0], (ivy.Device, ivy.NativeDevice)
                ):
                    ivy.utils.assertions.check_elem_in_list(
                        args[0],
                        [
                            "cpu",
                            "cuda",
                            "xpu",
                            "mkldnn",
                            "opengl",
                            "opencl",
                            "ideep",
                            "hip",
                            "ve",
                            "ort",
                            "mlc",
                            "xla",
                            "lazy",
                            "vulkan",
                            "meta",
                            "hpu",
                        ],
                    )
                if self.device == ivy.as_ivy_dev(args[0]):
                    return self
                else:
                    cast_tensor = self.clone()
                    cast_tensor.ivy_array = ivy.asarray(self.ivy_array, device=args[0])
                    return cast_tensor
        else:
            if (
                "dtype" in kwargs
                and "device" in kwargs
                and self.dtype == kwargs["dtype"]
                and self.device == kwargs["device"]
            ):
                return self
            else:
                cast_tensor = self.clone()
                cast_tensor.ivy_array = ivy.asarray(
                    self.ivy_array,
                    device=kwargs["device"] if "device" in kwargs else self.device,
                    dtype=kwargs["dtype"] if "dtype" in kwargs else self.dtype,
                )
                return cast_tensor

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arctan(self):
        return torch_frontend.atan(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arctan_(self):
        self.ivy_array = self.arctan().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "bfloat16")}, "torch")
    def arctan2(self, other):
        return torch_frontend.arctan2(self, other)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "bfloat16")}, "torch")
    def arctan2_(self, other):
        self.ivy_array = self.arctan2(other).ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def acos(self):
        return torch_frontend.acos(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def acos_(self):
        self.ivy_array = self.acos().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arccos(self):
        return torch_frontend.arccos(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def arccos_(self):
        self.ivy_array = self.arccos().ivy_array
        return self

    def new_tensor(
        self,
        data,
        *,
        dtype=None,
        device=None,
        requires_grad=False,
        layout=None,
        pin_memory=False,
    ):
        dtype = ivy.dtype(self.ivy_array) if dtype is None else dtype
        device = ivy.dev(self.ivy_array) if device is None else device
        _data = ivy.asarray(data, copy=True, dtype=dtype, device=device)
        return torch_frontend.tensor(_data)

    def view_as(self, other):
        return self.view(other.shape)

    def expand(self, *args, size=None):
        if args and size:
            raise TypeError("expand() got multiple values for argument 'size'")
        if args:
            if isinstance(args[0], (tuple, list)):
                size = args[0]
            else:
                size = args

        return torch_frontend.tensor(ivy.expand(self, tuple(size)))

    def expand_as(self, other):
        return self.expand(
            ivy.shape(other.ivy_array if isinstance(other, Tensor) else other)
        )

    def detach(self):
        return torch_frontend.tensor(
            ivy.stop_gradient(self.ivy_array, preserve_type=False)
        )

    def unsqueeze(self, dim):
        return torch_frontend.unsqueeze(self, dim)

    def unsqueeze_(self, dim):
        self.ivy_array = self.unsqueeze(dim).ivy_array
        return self

    def ravel(self):
        return torch_frontend.ravel(self)

    def split(self, split_size, dim=0):
        return torch_frontend.split(self, split_size, dim)

    def tensor_split(self, indices_or_sections, dim=0):
        return torch_frontend.tensor_split(self, indices_or_sections, dim)

    def vsplit(self, indices_or_sections=None, /, *, indices=None, sections=None):
        return torch_frontend.vsplit(
            self, indices_or_sections, indices=indices, sections=sections
        )

    def hsplit(self, indices_or_sections=None, /, *, indices=None, sections=None):
        return torch_frontend.hsplit(
            self, indices_or_sections, indices=indices, sections=sections
        )

    def dsplit(self, indices_or_sections=None, /, *, indices=None, sections=None):
        return torch_frontend.dsplit(
            self, indices_or_sections, indices=indices, sections=sections
        )

    def dim(self):
        return self.ivy_array.ndim

    def new_full(
        self,
        size,
        fill_value,
        *,
        dtype=None,
        device=None,
        requires_grad=False,
        layout=None,
        pin_memory=False,
    ):
        dtype = ivy.dtype(self.ivy_array) if dtype is None else dtype
        device = ivy.dev(self.ivy_array) if device is None else device
        _data = ivy.full(size, fill_value, dtype=dtype, device=device)
        return torch_frontend.tensor(_data)

    def new_empty(
        self,
        size,
        *,
        dtype=None,
        device=None,
        requires_grad=False,
        layout=None,
        pin_memory=False,
    ):
        dtype = ivy.dtype(self.ivy_array) if dtype is None else dtype
        device = ivy.dev(self.ivy_array) if device is None else device
        _data = ivy.empty(size, dtype=dtype, device=device)
        return torch_frontend.tensor(_data)

    def unfold(self, dimension, size, step):
        slices = []
        for i in range(0, self.shape[dimension] - size + 1, step):
            slices.append(self.ivy_array[i : i + size])
        return torch_frontend.stack(slices)

    def long(self, memory_format=None):
        self.ivy_array = ivy.astype(self.ivy_array, ivy.int64, copy=False)
        return self

    def max(self, dim=None, keepdim=False):
        return torch_frontend.max(self, dim=dim, keepdim=keepdim)

    def is_cuda(self):
        return "gpu" in ivy.dev(self.ivy_array)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def pow(self, exponent):
        return torch_frontend.pow(self, exponent)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def pow_(self, exponent):
        self.ivy_array = self.pow(exponent).ivy_array
        return self

    def size(self, dim=None):
        shape = ivy.shape(self.ivy_array)
        if dim is None:
            return shape
        else:
            try:
                return shape[dim]
            except IndexError:
                raise IndexError(
                    "Dimension out of range (expected to be in range of [{}, {}], "
                    "but got {}".format(len(shape), len(shape) - 1, dim)
                )

    def matmul(self, other):
        return torch_frontend.matmul(self, other)

    def argwhere(self):
        return torch_frontend.argwhere(self)

    def argmax(self, dim=None, keepdim=False):
        return torch_frontend.argmax(self, dim=dim, keepdim=keepdim)

    def argmin(self, dim=None, keepdim=False):
        return torch_frontend.argmin(self, dim=dim, keepdim=keepdim)

    def argsort(self, dim=-1, descending=False):
        return torch_frontend.argsort(self, dim=dim, descending=descending)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def ceil(self):
        return torch_frontend.ceil(self)

    def min(self, dim=None, keepdim=False):
        return torch_frontend.min(self, dim=dim, keepdim=keepdim)

    def permute(self, *args, dims=None):
        if args and dims:
            raise TypeError("permute() got multiple values for argument 'dims'")
        if dims is not None:
            return torch_frontend.permute(self, dims)
        if args:
            if isinstance(args[0], (tuple, list)):
                dims = args[0]
                return torch_frontend.permute(self, dims)
            else:
                return torch_frontend.permute(self, args)
        return torch_frontend.permute(self)

    def mean(self, dim=None, keepdim=False):
        return torch_frontend.mean(self, dim=dim, keepdim=keepdim)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def median(self, dim=None, keepdim=False):
        return torch_frontend.median(self, dim=dim, keepdim=keepdim)

    def transpose(self, dim0, dim1):
        return torch_frontend.transpose(self, dim0=dim0, dim1=dim1)

    def transpose_(self, dim0, dim1):
        self.ivy_array = self.transpose(dim0, dim1).ivy_array
        return self

    def t(self):
        return torch_frontend.t(self)

    def flatten(self, start_dim=0, end_dim=-1):
        return torch_frontend.flatten(self, start_dim, end_dim)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def cumsum(self, dim, dtype):
        return torch_frontend.cumsum(self, dim, dtype=dtype)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def cumsum_(self, dim, *, dtype=None):
        self.ivy_array = self.cumsum(dim, dtype).ivy_array
        return self

    def inverse(self):
        return torch_frontend.inverse(self)

    def neg(self):
        return torch_frontend.negative(self)

    def int(self, memory_format=None):
        self.ivy_array = ivy.astype(self.ivy_array, ivy.int32, copy=False)
        return self

    def bool(self, memory_format=None):
        self.ivy_array = ivy.astype(self.ivy_array, ivy.bool, copy=False)
        return self

    def type(self, dtype=None, non_blocking=False, **kwargs):
        if ivy.exists(dtype):
            self.ivy_array = ivy.astype(self.ivy_array, dtype)
            return self
        else:
            return str(self.dtype)

    def type_as(self, other):
        if self.dtype != other.dtype:
            self.ivy_array = ivy.astype(self.ivy_array, other.dtype)
            return self
        else:
            pass

    def byte(self, memory_format=None):
        self.ivy_array = ivy.astype(self.ivy_array, ivy.uint8, copy=False)
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def ne(self, other):
        return torch_frontend.ne(self, other)

    def squeeze(self, dim):
        return torch_frontend.squeeze(self, dim)

    def flip(self, dims):
        return torch_frontend.flip(self, dims)

    def fliplr(self):
        return torch_frontend.fliplr(self)

    def sort(self, dim=-1, descending=False):
        return torch_frontend.sort(self, dim=dim, descending=descending)

    def tril(self, diagonal=0):
        return torch_frontend.tril(self, diagonal=diagonal)

    def index_select(self, dim, index):
        return torch_frontend.index_select(self, dim, index)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "complex")}, "torch")
    def clamp(self, min=None, max=None):
        return torch_frontend.clamp(self, min=min, max=max)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "complex")}, "torch")
    def clamp_(self, min=None, max=None):
        self.ivy_array = self.clamp(min=min, max=max).ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "bfloat16")}, "torch")
    def sqrt(self):
        return torch_frontend.sqrt(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "bfloat16")}, "torch")
    def sqrt_(self):
        self.ivy_array = self.sqrt().ivy_array
        return self

    def where(self, condition, other):
        # TODO: replace with torch_frontend.where when it's added
        return torch_frontend.tensor(ivy.where(condition, self, other))

    def clone(self, memory_format=None):
        return torch_frontend.tensor(ivy.array(self.ivy_array, copy=True))

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def acosh(self):
        return torch_frontend.acosh(self)

    def real(self):
        return torch_frontend.real(self)

    def masked_fill(self, mask, value):
        # TODO: replace with torch_frontend.where when it's added
        return torch_frontend.tensor(ivy.where(mask, value, self))

    def masked_fill_(self, mask, value):
        self.ivy_array = self.masked_fill(mask, value).ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "bfloat16")}, "torch")
    def index_add_(self, dim, index, source, *, alpha=1):
        self.ivy_array = torch_frontend.index_add(
            self, dim, index, source, alpha=alpha
        ).ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def acosh_(self):
        self.ivy_array = self.acosh().ivy_array
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def numpy(self):
        return np_frontend_array(self.ivy_array)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def sigmoid(self):
        return torch_frontend.sigmoid(self)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def softmax(self, dim=None, dtype=None):
        return torch_frontend.nn.functional.softmax(self, dim=dim, dtype=dtype)

    def repeat(self, *args, repeats=None):
        if args and repeats:
            raise ivy.utils.exceptions.IvyException(
                "repeat() got multiple values for argument 'repeats'"
            )
        if args:
            if isinstance(args[0], (tuple, list)):
                repeats = args[0]
            else:
                repeats = args
        elif not isinstance(repeats, (tuple, list)):
            raise ivy.utils.exceptions.IvyException(
                "repeat(): argument 'repeats' must be tuple of ints"
            )

        return torch_frontend.tile(self, repeats)

    def unbind(self, dim=0):
        return torch_frontend.unbind(self, dim=dim)

    def bitwise_and_(self, other):
        self.ivy_array = self.bitwise_and(other).ivy_array

    @with_unsupported_dtypes({"1.11.0 and below": ("float16", "bfloat16")}, "torch")
    def atan2_(self, other):
        self.ivy_array = self.atan2(other).ivy_array
        return self

    def fmin(self, other):
        return torch_frontend.fmin(self, other)

    # Special Methods #
    # -------------------#

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __add__(self, other):
        return self.add(other)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __mod__(self, other):
        return torch_frontend.remainder(self, other)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __pow__(self, exponent):
        return self.pow(exponent)

    def __long__(self, memory_format=None):
        return self.long()

    def __getitem__(self, query, /):
        ivy_args = ivy.nested_map([self, query], _to_ivy_array)
        ret = ivy.get_item(*ivy_args)
        return torch_frontend.Tensor(ret, _init_overload=True)

    def __setitem__(self, key, value):
        key, value = ivy.nested_map([key, value], _to_ivy_array)
        self.ivy_array[key] = value

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __radd__(self, other):
        return torch_frontend.add(other, self)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __mul__(self, other):
        return torch_frontend.mul(self, other)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __rmul__(self, other):
        return torch_frontend.mul(other, self)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __sub__(self, other):
        return torch_frontend.subtract(self, other)

    def __truediv__(self, other):
        return torch_frontend.div(self, other)

    def __iadd__(self, other):
        ret = torch_frontend.add(self, other)
        self.ivy_array = ivy.inplace_update(
            self.ivy_array, ivy.astype(ret.ivy_array, self.dtype)
        )
        return self

    def __imod__(self, other):
        ret = torch_frontend.remainder(self, other)
        self.ivy_array = ivy.inplace_update(
            self.ivy_array, ivy.astype(ret.ivy_array, self.dtype)
        )
        return self

    def __imul__(self, other):
        ret = torch_frontend.mul(self, other)
        self.ivy_array = ivy.inplace_update(
            self.ivy_array, ivy.astype(ret.ivy_array, self.dtype)
        )
        return self

    def __isub__(self, other):
        ret = torch_frontend.subtract(self, other)
        self.ivy_array = ivy.inplace_update(
            self.ivy_array, ivy.astype(ret.ivy_array, self.dtype)
        )
        return self

    def __itruediv__(self, other):
        ret = torch_frontend.div(self, other)
        self.ivy_array = ivy.inplace_update(
            self.ivy_array, ivy.astype(ret.ivy_array, self.dtype)
        )
        return self

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __eq__(self, other):
        return torch_frontend.equal(self, other)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __gt__(self, other):
        return torch_frontend.greater(self, other)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __ne__(self, other):
        return self.ne(other)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __rsub__(self, other):
        return torch_frontend.subtract(other, self)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __lt__(self, other):
        return torch_frontend.less(self, other)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def __or__(self, other):
        return torch_frontend.bitwise_or(self, other)

    def __invert__(self):
        return torch_frontend.bitwise_not(self)

    def __and__(self, other):
        return torch_frontend.bitwise_and(self, other)

    # Method aliases
    absolute, absolute_ = abs, abs_
    clip, clip_ = clamp, clamp_
    ndimension = dim

    def bitwise_xor(self, other):
        return torch_frontend.bitwise_xor(self, other)

    @with_unsupported_dtypes({"1.11.0 and below": ("float16",)}, "torch")
    def cumprod(self, dim, dtype):
        return torch_frontend.cumprod(self, dim, dtype=dtype)

    def count_nonzero(self, dim):
        return torch_frontend.count_nonzero(self, dim=dim)

    @with_unsupported_dtypes({"1.11.0 and below": ("bfloat16",)}, "torch")
    def exp(self):
        return torch_frontend.exp(self)

    def mul(self, other):
        return torch_frontend.mul(self, other)
