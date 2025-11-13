import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity, Image, ActivityIndicator } from 'react-native';
import axios from 'axios';

export default function HomeScreen({ navigation }) {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const res = await axios.get('http://192.168.1.10:3000/api/headlines'); // Replace with your backend API
        setArticles(res.data.articles); // adapt this depending on your API response
      } catch (err) {
        console.log(err);
      } finally {
        setLoading(false);
      }
    };
    fetchArticles();
  }, []);

  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={styles.headlineCard}
      onPress={() => navigation.navigate('Article', { article: item })}
    >
      {item.image && <Image source={{ uri: item.image }} style={styles.headlineImage} />}
      <Text style={styles.headlineText}>{item.title}</Text>
    </TouchableOpacity>
  );

  if (loading) return <ActivityIndicator size="large" style={{ flex: 1 }} />;

  return (
    <View style={styles.container}>
      <FlatList
        data={articles}
        keyExtractor={(item, index) => index.toString()}
        renderItem={renderItem}
        showsVerticalScrollIndicator={false}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f2f5',
    padding: 10,
  },
  headlineCard: {
    backgroundColor: '#fff',
    padding: 15,
    marginVertical: 8,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  headlineText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    marginTop: 5,
  },
  headlineImage: {
    width: '100%',
    height: 180,
    borderRadius: 10,
  },
});
