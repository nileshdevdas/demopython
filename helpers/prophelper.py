class PropertyHelper:
    def __init__(self):
        self.props = {};
        config =open("d:/config.properties");
        for line in config:
            data = line.strip().split(":");
            self.props[data[0]]=data[1];
