from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Score, Post


@receiver(post_save, sender=Score)
def update_post_score(sender, instance, created, **kwargs):
    if created:
        # for first creating score object
        print("score signal triggered.")
        post_obj = Post.objects.get(pk=instance.post.pk)

        last_total_scores = post_obj.countOfUsers * post_obj.meadPostScore
        post_obj.countOfUsers += 1
        post_obj.meadPostScore = (
            last_total_scores + instance.value) / post_obj.countOfUsers
        post_obj.save()


