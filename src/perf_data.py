class PerfData(object):
    def __init__(self):
        self.event_data_ = dict()
    
    def get_event_data(self, event_name):
        data = self.event_data_[event_name]
        return data

class SingleProcessPerfData(PerfData):
    
    def get_event_data_s(self, event_name, pid = -1, tid = -1):
        data = self.get_event_data(event_name)
        if pid == -1 and tid == -1:
            return data
        elif tid == -1:
            return data[pid]
        else:
            return data[pid][tid] 


class MultiProcessPerfData(PerfData):
    
    def get_event_data_m(self, event_name, tid = -1):
        data = self.get_event_data(event_name)
        if tid == -1:
            return data
        else:
            return data[tid] 