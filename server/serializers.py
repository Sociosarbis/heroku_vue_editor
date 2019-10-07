from marshmallow import Schema, fields


class User_English_Link_Schema(Schema):
  user_id = fields.Str()
  English_id = fields.Str()
  tag_name = fields.Str()

class Tag_Schema(Schema):
  name = fields.Str()
  links = fields.Nested(User_English_Link_Schema, many=True)

tag_schema = Tag_Schema()
tags_schema = Tag_Schema(many=True)
user_English_link_schema = User_English_Link_Schema()