import rules


@rules.predicate
def is_post_author(blogger, post):
    return post.author == blogger


rules.add_perm('blogs.add_post', rules.is_authenticated)
rules.add_perm('blogs.change_post', is_post_author)
rules.add_perm('blogs.delete_post', is_post_author | rules.is_superuser)
