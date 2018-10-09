from django.contrib import admin
from .models import District, Company, Category, EnterpriseNetwork, Product, CompanyProduct


class CompanyProductInline(admin.TabularInline):
    model = CompanyProduct
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = (CompanyProductInline,)


admin.site.register(District)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Category)
admin.site.register(EnterpriseNetwork)
admin.site.register(Product)
