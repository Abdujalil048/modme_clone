from rest_framework.serializers import ModelSerializer

from users.models import Lead, LeadIncrement


class LeadModelSerializer(ModelSerializer):
    class Meta:
        model = Lead
        fields = ('phone', 'full_name', 'comment', 'lead_increment', 'status')


class LeadIncrementModelSerializer(ModelSerializer):
    class Meta:
        model = LeadIncrement
        fields = ('name',)
