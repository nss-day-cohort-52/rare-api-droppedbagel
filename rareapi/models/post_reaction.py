from django.db import models

class PostReaction(models.Model):
    user = models.ForeignKey("theUser", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_reactions")
    reaction = models.ForeignKey("Reaction", on_delete=models.CASCADE)