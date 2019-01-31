from urllib import robotparser

def parse_robot(url):
    """
    Parsing websites robot.txt files using urllib
    """
    robot_parser = robotparser.RobotFileParser()
    robot_parser.set_url(url)
    robot_parser.read()
    return robot_parser
