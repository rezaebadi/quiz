# Django Coding Questions

1. **Custom Model Manager**  
   Write a `PublishedManager` for a `Post` model (with an `is_published` BooleanField) so that `Post.published.all()` returns only published posts.

2. **Automatic Profile Creation**  
   Ensure a `Profile` is created automatically when a new `User` is registered.

3. **Avoiding N+1 Queries**  
   Optimize a query to list all books and their authors without triggering N+1 queries.

4. **Dynamic ModelForm Fields**  
   Build a `ModelForm` that dynamically creates form fields from a `questions_json` field in the `Survey` model.

5. **Generic Tagging System**  
   Implement tagging using Django's `ContentType` framework so any model (e.g., `Photo`) can have tags.

6. **Nested JSON API with DRF**  
   Using Django REST Framework, build a nested serializer for `Company` → `Employee`.

7. **Tenant-Aware Middleware**  
   Write middleware to extract subdomain from the request and attach the corresponding `Tenant` object to `request.tenant`.
