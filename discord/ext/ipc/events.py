from hikari import Event

class IPCEvent(Event):
	"""Base class for IPC events."""

	def __init__(
			self,
			name: str,
			endpoint: str | None,
			error: Exception | None
		) -> None:
		super().__init__()

		self.name = name
		self.endpoint = endpoint
		self.error = error

class IPCError(IPCEvent):
	"""Raised when an error occurs during an IPC request."""

	def __init__(
			self,
			endpoint: str | None,
			error: Exception
		) -> None:
		super().__init__("ipc_error", endpoint, error)

class IPCReady(IPCEvent):
	"""Raised when the IPC server is ready to accept connections."""

	def __init__(self) -> None:
		super().__init__("ipc_ready", None, None)