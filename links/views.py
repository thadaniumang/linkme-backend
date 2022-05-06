from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .models import LinkList, Links
from .serializers import GetLinkSerializer, LinkListSerializer, LinkSerializer


# Create your views here.
class GetLinks(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = GetLinkSerializer
    
    def get(self, request, list_id):
        try:
            link_list = LinkList.objects.get(id=list_id)
            links = Links.objects.filter(link_list=link_list)
            list_dict = dict()
            count = 0
            
            for link in links:
                list_dict.update({
                    "{}".format(count): {
                        "id": link.id,
                        "title": link.title,
                        "url": link.link
                    }
                })
                count += 1
            
            return Response(list_dict, status = status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid List ID'
            }, status = status.HTTP_400_BAD_REQUEST)
            

class CreateNewList(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LinkListSerializer
    
    def post(self, request):
        data = request.data
        
        link_list = dict()
        link_list['title'] = data.get('title')
        link_list['profile'] = request.user.profile.pk
        
        serializer = self.serializer_class(data = link_list)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            
        return Response({
            'message': 'Created',
            'link_list': serializer.data
        })


class GetLists(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = LinkListSerializer
    
    def get(self, request):
        try:
            link_lists = LinkList.objects.filter(profile=request.user.profile.pk)
            list_dict = dict()
            count = 0
            
            for lists in link_lists:
                print(lists)
                list_dict.update({
                    "{}".format(count): {
                        "title": lists.title,
                        "id": lists.id
                    }
                })
                count += 1
            
            return Response(list_dict, status = status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Request'
            }, status = status.HTTP_400_BAD_REQUEST)


class GetListCreator(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = LinkListSerializer
    
    def get(self, request, list_id):
        try:
            link_lists = LinkList.objects.get(id=list_id)
                        
            return Response({
                "username": link_lists.username
            }, status = status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Request'
            }, status = status.HTTP_400_BAD_REQUEST)


            
class CreateLinks(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LinkSerializer
    
    def post(self, request):
        data = request.data
        
        link = dict()
        link['link_list'] = data.get('list_id')
        link['title'] = data.get('title')
        link['link'] = data.get('link')
        
        serializer = self.serializer_class(data = link)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            
        return Response({
            'message': 'Created',
            'link': serializer.data
        })


class DeleteLink(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LinkSerializer
    
    def delete(self, request, link_id):
        Links.objects.filter(id=link_id).delete()
        return Response({
            'message': 'Deleted'
        })


class DeleteList(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LinkListSerializer
    
    def delete(self, request, list_id):
        LinkList.objects.filter(id=list_id).delete()
        return Response({
            'message': 'Deleted'
        })