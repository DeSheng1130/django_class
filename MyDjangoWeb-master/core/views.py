from django.shortcuts import render


def hi(request, n1, n2):
    s = n1 + n2
    return render(request, 'hi.html', {
        's': s,
    })


def r(request, start, stop):
    if start > stop:
        start, stop = stop, start

    rr = range(start, stop+1)
    if start > stop:
        rr = reversed(rr)

    return render(request, 'r.html', {
        'rr': rr,
    })


def tag_test(request):
    ll = [1, 2, 3, 4, 5, 6, 7, 8]
    return render(request, 'tag_test.html', {
        'll': ll
    })
















