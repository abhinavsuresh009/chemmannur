from rest_framework.decorators import api_view
from rest_framework.response import Response
from companybranch.models import Branch
from companybranch.serializers.branch import BranchSerializer
from rest_framework import status


# Views for Branch

@api_view(['GET','POST','DELETE','PATCH'])
def branch(request):
    brcode = request.query_params.get('brcode', None)
    comcode = request.query_params.get('comcode', None)

# GET Method

    if request.method == 'GET':
        companies = Branch.objects.all()
        serializer = BranchSerializer(companies, many=True,context = {'comcode' : comcode})
        return Response({'message' : 'Here is your Data', 'status_code' : '200' , 'data' : serializer.data})
    
# POST Method
    elif request.method == 'POST':
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Create successfully', 'status_code' : '200' , 'data' : serializer.data}, status=status.HTTP_200_OK )
        else:
            return Response({'message' : 'Error found', 'status_code' : '400' , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
# DELETE Method
    elif request.method == 'DELETE':
        if brcode:
            serializer = Branch.objects.filter(brcode = brcode)
            serializer.delete()
        return Response({'message' : 'Deleted successfully', 'status_code' : '200' , 'data' : serializer.data}, status=status.HTTP_204_NO_CONTENT)
    
# UPDATE Method
    elif request.method == 'PATCH':
        if brcode:
            branches = Branch.objects.filter(brcode=brcode)
            if branches.exists():
                branch = branches.first()
                serializer = BranchSerializer(branch, data=request.data, partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message' : 'Updated successfully', 'status_code' : '200' , 'data' : serializer.data})
                return Response({'message' : 'Error found', 'status_code' : '400' , 'error' : serializer.errors} , status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Branch not found', 'status_code': '404'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'brcode parameter is required for PUT/PATCH method', 'status_code': '400'}, status=status.HTTP_400_BAD_REQUEST)
