def paginate(items, page, size):
    if (isinstance(page, bool) or not isinstance(page, int) or page <= 0
            or isinstance(size, bool) or not isinstance(size, int) or size <= 0):
        raise ValueError("page and size must be positive integers")
    offset = (page - 1) * size
    return items[offset:offset + size]
