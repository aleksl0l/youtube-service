import django_filters


class VideosFilter(django_filters.FilterSet):
    date__gte = django_filters.DateFilter(field_name="published_at", lookup_expr="gt", input_formats=["%d.%m.%Y"])
    date__lte = django_filters.DateFilter(field_name="published_at", lookup_expr="lt", input_formats=["%d.%m.%Y"])
