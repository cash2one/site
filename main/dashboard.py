# -*- coding: utf-8 -*-
from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(modules.ModelList(
            u'Модули сайта',
            collapsible=True,
            column=1,
            css_classes=('collapse open',),
            models=(
                'flatpages.models.IndexPage',
                'flatpages.models.IndexAbout',
                'flatpages.models.FlatPage',
                'flatpages.models.Advantage',
                'flatpages.models.Manager',
                'announce.models.Announce',
                'placeholder.models.Placeholder',
                # 'services.models.Service',
                'slider.models.Slide',
                'mapelements.models.MapPoint',
            ),
        ))

        self.children.append(modules.ModelList(
            u'Новости',
            collapsible=True,
            column=1,
            css_classes=('collapse open',),
            models=(
                'news.models.News',
                # 'news.models.Blog_Tag',
            ),
        ))

        self.children.append(modules.ModelList(
            u'Адресная программа',
            collapsible=True,
            column=1,
            css_classes=('collapse open',),
            models=(
                'addressprogram.models.*',
            ),
        ))

        self.children.append(modules.ModelList(
            u'Заказы',
            collapsible=True,
            column=1,
            css_classes=('collapse open',),
            models=(
                'order.models.*',
            ),
        ))

        self.children.append(modules.ModelList(
            u'Дополнительно',
            collapsible=True,
            column=1,
            css_classes=('collapse open',),
            models=(
                'error_manag.models.*',
                'message.models.Mail',
                'message.models.Message',
                'feedback.models.Feedback'
            ),
        ))

        self.children.append(modules.LinkList(
            u'Быстрые ссылки',
            column=2,
            children=[
                {
                    'title': u'Менеджер файлов',
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
                {
                    'title': u'Настройки SEO',
                    'url': '/admin/sites/site/1/',
                    'external': False,
                },
                {
                    'title': u'Настройки сайта',
                    'url': '/admin/constance/config',
                    'external': False,
                },
            ]
        ))

        self.children.append(modules.RecentActions(
            u'Последние действия',
            limit=7,
            collapsible=False,
            column=2,
        ))