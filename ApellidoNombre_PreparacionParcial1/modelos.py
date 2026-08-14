

class User:

    def __init__(self, id, name, email, role):
        self.id = id
        self.name = name
        self.email = email
        self.role = role

    def __str__(self):
        return f"{self.name} - {self.email} - {self.role}"


class Ticket:

    def __init__(
        self,
        id,
        title,
        category,
        priority,
        status="Open"
    ):
        self.id = id
        self.title = title
        self.category = category
        self.priority = priority
        self.status = status

    def change_status(self, new_status):
        self.status = new_status


class Comment:

    def __init__(self, id, content, created_at):
        self.id = id
        self.content = content
        self.created_at = created_at

    def add_comment(self):
        pass


class History:

    def __init__(self, id, action, created_at):
        self.id = id
        self.action = action
        self.created_at = created_at

    def record_action(self):
        pass


class Article:

    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def publish(self):
        pass