from rest_framework import serializers
from .models import Detail, Mark

class Detail_Serializers(serializers.ModelSerializer):
    """
    Ref-Model : Detail
    """
    class Meta:
        model = Detail
        fields = '__all__'

class Mark_Serializers(serializers.ModelSerializer):
    """
        Ref-Model : Mark

    """
    class Meta:
        model = Mark
        fields = '__all__'

    def to_representation(self, instance):
        """
            To get ForeignKey Field Name Instead of id
        """
        rep = super(Mark_Serializers, self).to_representation(instance)
        rep['student'] = instance.student.name
        return rep
