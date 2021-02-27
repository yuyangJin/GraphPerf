class LineInfo(object):
    def __init__(self, 
                dir_name_, 
                file_name_,
                line_num_
                ):
        self.dir_name_ = dir_name_
        self.file_name_ = file_name_
        self.line_num_ = line_num_
    
    def get_dir_name(self):
        return self.dir_name_
    
    def get_file_name(self):
        return self.file_name_
    
    def get_line_num(self):
        return self.line_num_