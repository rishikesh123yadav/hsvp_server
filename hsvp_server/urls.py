"""hsvp_server URL Configuration

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


from django.conf.urls import url
from hsvp.views import SellerViewSet
from hsvp.views import AddressViewSet
from django.contrib import admin
from django.urls import path, include
from hsvp.views import UserViewSet
from hsvp.views import BidderViewSet
from hsvp.views import AddressViewSet
from hsvp.views import ItemViewSet
from hsvp.views import AuctionDetailViewSet
from hsvp.views import DocumentViewSet
from hsvp.views import AuctionViewSet
from hsvp.views import EMDViewSet
from hsvp.views import BidViewSet
from hsvp.views import RoundViewSet
from hsvp.views import UserDocumentViewSet
from hsvp.views import BankDetailViewSet
from hsvp.views import AuctionDocumentViewSet
from hsvp.views import JointHolderViewSet
from django.conf import settings
from django.conf.urls.static import static
from hsvp.views import UploadFile
from hsvp import views

if getattr(settings, 'DEBUG', False) or getattr(settings, 'SANDBOX', False):
    # let the user browse the API if DEBUG is True
    # /api/ will return a list of available routes
    from rest_framework.routers import DefaultRouter as DRFSimpleRouter
else:
    # user shouldn't be able to browse the API
    # /api/ will return 404
    from rest_framework.routers import SimpleRouter as DRFSimpleRouter

router = DRFSimpleRouter()

router.register('seller', SellerViewSet)
router.register('user', UserViewSet)
router.register('bidder', BidderViewSet)
router.register('document', DocumentViewSet)
router.register('auction-detail', AuctionDetailViewSet)
router.register('item', ItemViewSet)
router.register('address', AddressViewSet)
router.register('auction', AuctionViewSet)
router.register('emd', EMDViewSet)
router.register('bid', BidViewSet)
router.register('round', RoundViewSet)
router.register('bank-detail', BankDetailViewSet)
router.register('user-document', UserDocumentViewSet)
router.register('auction-document', AuctionDocumentViewSet)
router.register('joint-holder', JointHolderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    url('api/upload/', views.UploadFile.as_view(), name='upload-test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
