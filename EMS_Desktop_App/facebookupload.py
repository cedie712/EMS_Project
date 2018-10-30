import facebook
from models import EMS_db_model

class FbUpload:
    def __init__(self, memo, imagex=None):
        self.memo = memo
        self.img = imagex
        self.db = EMS_db_model()
        self.config = self.db.get_config()[0]
        self.fb_id = self.config['fb_page_id']
        self.user_token = self.config['fb_user_token']

        cfg = {
            "page_id": self.fb_id,
            "access_token": self.user_token,
        }

        api = self.get_api(cfg)
        if self.img is None:
            api.put_object('me', 'feed', message=self.memo)
        else:
            api.put_photo(image=open(self.img, 'rb'), message=self.memo)

    def get_api(self ,cfg):
        graph = facebook.GraphAPI(cfg['access_token'])
        resp = graph.get_object('me/accounts')
        page_access_token = None
        for page in resp['data']:
            if page['id'] == cfg['page_id']:
                page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
        return graph
