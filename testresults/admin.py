from django.contrib import admin
from testresults.models import Package
from testresults.models import Repository
from testresults.models import Branch
from testresults.models import Commit
from testresults.models import TestClass
from testresults.models import TestMethod
from testresults.models import TestEnvironment
from testresults.models import TestExecution
from testresults.models import TestResult

class PackageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Package, PackageAdmin)

class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('name','package','url')
    list_filter = ('package',)
admin.site.register(Repository, RepositoryAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name','package','repository','url')
    list_filter = ('package','repository')
admin.site.register(Branch, BranchAdmin)

class CommitAdmin(admin.ModelAdmin):
    list_display = ('name','package','repository','branch','commit_date','url')
    list_filter = ('package','repository','branch')
admin.site.register(Commit, CommitAdmin)

class TestClassAdmin(admin.ModelAdmin):
    list_display = ('name','package')
    list_filter = ('package',)
admin.site.register(TestClass, TestClassAdmin)

class TestMethodAdmin(admin.ModelAdmin):
    list_display = ('name','testclass')
    list_filter = ('testclass',)
admin.site.register(TestMethod, TestMethodAdmin)

class TestEnvironmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(TestEnvironment, TestEnvironmentAdmin)

class TestExecutionAdmin(admin.ModelAdmin):
    list_display = ('name','package','repository','branch','commit','environment')
    list_filter = ('package','repository','branch','environment')
admin.site.register(TestExecution, TestExecutionAdmin)

class TestResultAdmin(admin.ModelAdmin):
    list_display = ('id','execution','method','outcome','duration','worst_limit','worst_limit_percent')
    list_filter = ('method',)
admin.site.register(TestResult, TestResultAdmin)

