from rest_framework.decorators import api_view
from rest_framework.response import Response
from companybranch.models import Branch
from companybranch.serializers.branch import BranchSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def branches(request, comcode: str):
    try:
        branches = Branch.objects.filter(company=comcode)
        if not branches.exists():
            return Response({"error": "No branches found for the given company code.", 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
        serializer = BranchSerializer(branches, many=True)
        return Response({"success": "Branches fetched successfully.", 'status_code': 200, "data": serializer.data})
    except:
        return Response({"error": "Server error occurred.", 'status_code': 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Views for Branch
@api_view(['GET'])
def branch(request, comcode: str):
# GET Method
    brname = request.query_params.get('brname')
    try:
        branches = Branch.objects.filter(company=comcode)   
        if brname:
            branches = branches.filter(brname__istartswith=brname)
        if not branches.exists():
            return Response({"error": "No Branches found.", 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Number of items per page
        result_page = paginator.paginate_queryset(branches, request)
        serializer = BranchSerializer(result_page, many=True)
        return paginator.get_paginated_response({"success": "filtered success.", 'status_code': 200, "data":serializer.data})
    except:
        return Response({"error": "server error", 'status_code': 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# POST Method
@api_view(['POST'])
def create_branch(request):
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'Branch is created successfully', 'status_code' : 201 , 'data' : serializer.data}, status= status.HTTP_201_CREATED)
    return Response({'message': 'error occured', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# DELETE and UPDATE Method  
@api_view(['PATCH', 'DELETE'])
def branch_delete_update(request):
    brcode = request.query_params.get('brcode', None)
    if not brcode:
        return Response({'error': 'brcode parameter is required for DELETE/UPDATE method', 'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)
    try:
        branch = Branch.objects.get(brcode=brcode)
    except Branch.DoesNotExist:
        return Response({'error': 'Branch not found', 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        branch.delete()
        return Response({'success': 'Deleted successfully', 'status_code': 204 }, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        serializer = BranchSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated successfully', 'status_code': 201, 'data': serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'message': 'error occured', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
