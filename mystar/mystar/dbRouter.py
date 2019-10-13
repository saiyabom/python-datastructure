


class DBRouter(object):
    def db_for_read(self, model,**hints):
        print('>>>model for read:',model)
        if model._meta.app_label == 'model2':
            return 'secondary'
        return 'default'
    def db_for_write(self, model,**hints):
        print('>>>model for write: ', model)
        if model._meta.app_label == 'model2':
            return 'secondary'
        return 'default'
