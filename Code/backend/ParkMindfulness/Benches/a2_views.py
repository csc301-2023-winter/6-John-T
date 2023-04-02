from django.shortcuts import render, redirect
from .forms import BenchesCreateForm, BenchesUpdateForm, BenchesDeleteForm
from .models import Benches

## This views.py file contains the simple function views to be used alongside the django forms
## we HAD TO make use of to have a working UI through Django. The actual CRUD API views are in the
## RESTviews.py file which contains the class-based views that will be used in the actual project, but
## given the format of the assignment, this is what we have been force to do.

# simple view for bench creation
def bench_create(request):
    if request.method == 'POST':
        # upon post, load up the appropriate form
        form = BenchesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # if data in the form is validated, we save the new object in DB
            form.save()
            # reload, send user back to the same create view (this method)
            return redirect('bench_view')
    else:
        # initial load of the form when no data has been entered
        form = BenchesCreateForm()
    # render the form. form is the context variable we'll use in the template with {{}}
    return render(request, 'create.html', {'form': form})


# simple view for bench viewing (getting all objects)
def bench_view(request):
    # get all benches from the DB (filtering and such would be available through our REST API)
    benches = Benches.objects.all()
    # render the view with the context variable loaded with all the benches
    return render(request, 'view.html', {'benches': benches})


# simple view for bench updating
def bench_update(request, bench_id):
    # get the bench to update in the DB
    bench = Benches.objects.get(bench_id=bench_id)
    if bench is None:
        # if the bench is not found, send user back to the view view
        return redirect('bench_view')
    
    if request.method == 'POST':
        # upon post, load up the appropriate form
        form = BenchesUpdateForm(request.POST, request.FILES, instance=bench)
        if form.is_valid():
            # if data in the form is validated, we save the updated object in DB
            form.save()
            # reload, send user back to the view view
            return redirect('bench_view')
    
    # otw, load a dummy form
    # load the form with the bench data
    form = BenchesUpdateForm(instance=bench)
    # render the form. form is the context variable we'll use in the template with {{}}
    return render(request, 'update.html', {'form': form})


# simple view for bench deletion
def bench_delete(request, bench_id):
    # get the bench to delete in the DB
    bench = Benches.objects.get(bench_id=bench_id)
    if bench is None:
        # if the bench is not found, send user back to the view view
        return redirect('bench_view')
    
    if request.method == 'POST':
        # delete the bench after button press
        bench.delete()
        # reload, send user back to the view view
        return redirect('bench_view')
        
    # reload, send user back to the view view
    return render(request, 'delete.html', {'bench': bench})