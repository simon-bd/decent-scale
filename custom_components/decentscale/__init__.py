import asyncio
from pydecentscale import DecentScale

class DecentScaleHub:
    def __init__(self):
        self.ds = DecentScale()
        self._callbacks = []
    def register_callback(self, callback):
        self._callbacks.append(callback)
    async def connect(self):
        # Run blocking connect in executor if needed
        await self.ds.auto_connect()
        await self.ds.enable_notification()
        # In practice, pydecentscale example is sync; adapt accordingly.
        self.ds.on_weight_change = self._handle_weight
    def _handle_weight(self, weight):
        # Called on BLE notification
        for cb in self._callbacks:
            cb()  # sensors update themselves by pulling state
    @property
    def weight(self):
        return self.ds.weight
    @property
    def timer(self):
        return self.ds.timer
