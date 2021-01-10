"""
all views and viewsets import
make sure to create each view and viewsets in different file
"""
from .seller import SellerViewSet
from .user import UserViewSet
from .bidder import BidderViewSet
from .document import DocumentViewSet
from .auction_detail import AuctionDetailViewSet
from .item import ItemViewSet
from .address import AddressViewSet
from .auction import AuctionViewSet
from .emd import EMDViewSet
from .bid import BidViewSet
from .round import RoundViewSet
from .user_document import UserDocumentViewSet
from .auction_document import AuctionDocumentViewSet
from .bank_detail import BankDetailViewSet
from .joint_holder import JointHolderViewSet
from .upload import UploadFile
