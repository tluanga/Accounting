"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from acm.cashbook.views import DayBookViewSet, LedgerViewSet, CashBookViewSet, LedgerMasterViewSet
from acm.trial.views import TrialBalanceViewSet
from acm.finalacc.views import TradingAccountViewSet

router = DefaultRouter()
router.register('master', LedgerMasterViewSet)
router.register('daybook', DayBookViewSet)
router.register('ledger', LedgerViewSet)
router.register('cashbook', CashBookViewSet)
router.register('trialbalance', TrialBalanceViewSet)
router.register('tradingaccount', TradingAccountViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), name='home'),
    path('auth/', include('acm.account.urls'))
]
